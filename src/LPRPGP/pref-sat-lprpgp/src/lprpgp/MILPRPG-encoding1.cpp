/************************************************************************
 * Copyright 2008, 2009, Strathclyde Planning Group,
 * Department of Computer and Information Sciences,
 * University of Strathclyde, Glasgow, UK
 * http://planning.cis.strath.ac.uk/
 *
 * Maria Fox, Richard Howey and Derek Long - Code from VAL
 * Stephen Cresswell - PDDL Parser
 * Andrew Coles, Amanda Coles - Code for LPRPG
 *
 * This file is part of LPRPG.
 *
 * LPRPG is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * LPRPG is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with LPRPG.  If not, see <http://www.gnu.org/licenses/>.
 *
 ************************************************************************/

#include "MILPRPG.h"
#include "RPGBuilder.h"

#include <sstream>
#include <string>

using std::ostringstream;
using std::string;

namespace Planner {


vector<map<int, MILPRPG::ActionEffectUponVariable> > MILPRPG::preprocessedData;
int MILPRPG::actCount;


MILPRPG::MILPRPG(MinimalState * f, const vector<double> & layerZero) : varCount(layerZero.size()), colCount(varCount), startingState(f) {

	static bool donePreprocessing = false;

	if (!donePreprocessing) {

		preprocessedData = vector<map<int, ActionEffectUponVariable> >(varCount);
		
		vector<RPGBuilder::RPGNumericEffect> & numericEffs = RPGBuilder::getNumericEffs();
		vector<list<int> > & actEffs = RPGBuilder::getActionsToRPGNumericStartEffects();

		actCount = actEffs.size();
		for (int i = 0; i < actCount; ++i) {
			list<int>::iterator effItr = actEffs[i].begin();
			const list<int>::iterator effEnd = actEffs[i].end();

			for (; effItr != effEnd; ++effItr) {
				RPGBuilder::RPGNumericEffect & currEff = numericEffs[*effItr];
				double quickEff = currEff.evaluate(layerZero);
				preprocessedData[currEff.fluentIndex].insert(pair<int, ActionEffectUponVariable>(i, ActionEffectUponVariable(quickEff, currEff.isAssignment)));				
			}

		}

		donePreprocessing = true;
	}

	lp = make_lp(0,varCount);
	
	set_verbose(lp,3);


	for (int i = 1; i <= varCount; ++i) {

		const double curr = layerZero[i-1];
		set_bounds(lp,i,curr,curr);
		
		ostringstream namestream;
		namestream << *(RPGBuilder::getPNE(i - 1));
		namestream << "[0.000]";
		string asString = namestream.str();
		set_col_name(lp, i, const_cast<char*>(asString.c_str()));
	}

	vector<VarData> mmv(varCount * 2);

	for (int i = 0; i < varCount; ++i) {

		mmv[i].Vvar = i + 1;
		mmv[i].SUvar = 1;

	}


	minMaxVars.insert(pair<double, vector<VarData> >(0.0, mmv));

	if (varCount) {
		static REAL maximise[1];
		maximise[0] = -1.0;
		static int optVar[1];		
		optVar[0] = 1;

//		set_minim(lp);
		set_obj_fnex(lp, 1, maximise, optVar);
	
	}

//	print_lp(lp);

};



MILPRPG::~MILPRPG() {

	delete_lp(lp);

};

void MILPRPG::addApplicableActions(vector<int> * const propPrec, vector<int> * const numPrec) {

	const bool debugAdd = false;

	pair<const double, vector<VarData> > & prev = *(minMaxVars.rbegin());
	const double actTS = prev.first;
	const double factTS = actTS + 1.0;

	vector<VarData> & newVars = minMaxVars.insert(pair<double, vector<VarData> >(factTS, prev.second)).first->second;

	map<int, ActData> & actionVars = layerActionVariables[actTS];

	{
		const int ailSize = propPrec->size();
		for (int i = 0; i < ailSize; ++i) {
			if (!((*propPrec)[i]) && !((*numPrec)[i])) {
				pair<map<int,bool>::iterator, bool> insItr = applicableSoFar.insert(pair<int, bool>(i,true));
				if (insItr.second == true) {
					const bool intr = RPGBuilder::isInteresting(i, startingState->first, startingState->startedActions);
					if (!intr) {
						insItr.first->second = false;
					} else {
						actionVars.insert(pair<int, ActData>(i, ActData()));
						const int howMany = RPGBuilder::howManyTimes(i, *startingState);
						if (howMany != INT_MAX) {
							static const list<int> emptyList;
							boundedActs[i] = pair<int, int>(howMany, -1);
						}
					}
				} else {
					if (insItr.first->second) actionVars.insert(pair<int, ActData>(i, ActData()));
				}
			}
		}
	}

	

	{
		map<int, ActData>::iterator actItr = actionVars.begin();
		const map<int, ActData>::iterator actEnd = actionVars.end();
	
		for (; actItr != actEnd; ++actItr) {
			add_columnex(lp,0,0,0);
			actItr->second.Avar = ++colCount;
			set_bounds(lp,actItr->second.Avar,0,1);

			map<int, pair<int, int> >::iterator baItr = boundedActs.find(actItr->first);
			if (baItr != boundedActs.end()) {
				if (baItr->second.second == -1) {
					baItr->second.second = get_Nrows(lp);
					static REAL varWeight[1];
					varWeight[0] = 1.0;
					static int theVar[1];
					theVar[0] = actItr->second.Avar;
					if (debugAdd) cout << "Action " << theVar[0] << " added to a " << baItr->second.first << "-shot set\n";
					add_constraintex(lp, 1, varWeight, theVar, LE, baItr->second.first);
				} else {
					set_mat(lp, baItr->second.second, actItr->second.Avar, 1.0);
					if (debugAdd) cout << "Action " << actItr->second.Avar << " added to a " << baItr->second.first << "-shot set, row " << baItr->second.second << "\n";
				}
			}
		}
	}
	
	for (int i = 0; i < varCount; ++i) {
		add_columnex(lp,0,0,0);
		newVars[i].Vvar = ++colCount;
//		add_columnex(lp,0,0,0);
//		newVars[i].SUvar = ++colCount;

//		set_bounds(lp, newVars[i].SUvar,0,1);
  		set_lowbo(lp,newVars[i].Vvar,0);
//		set_bounds(lp, newVars[i].Vvar,0.0,1.01);

		ostringstream namestream;
		namestream << *(RPGBuilder::getPNE(i));
		namestream << "[" << factTS << "]";
		string asString = namestream.str();
		set_col_name(lp, newVars[i].Vvar, const_cast<char*>(asString.c_str()));
	}

	static REAL* actWeight = new REAL[actCount + 2];
	static int* colno = new int[actCount + 2];

	static REAL* assActWeight = new REAL[actCount];
	static int* assColno = new int[actCount];


	assert(colCount == get_Ncolumns(lp));

	for (int i = 0; i < varCount; ++i) {
		if (debugAdd) cout << "Building value constraint for variable " << i << " - " << *(RPGBuilder::getPNE(i)) << "\n";
		int arrSize = 2;
		int assSize = 0;
		actWeight[0] = 1.0;
		actWeight[1] = -1.0;
		colno[0] = prev.second[i].Vvar;
		colno[1] = newVars[i].Vvar;


		if (debugAdd) cout << "Bounds on new value: [" << get_lowbo(lp, colno[1]) << "," << get_upbo(lp, colno[1]) << "]\n";
		if (debugAdd) cout << "Bounds on previous value: [" << get_lowbo(lp, colno[0]) << "," << get_upbo(lp, colno[0]) << "]\n";

		if (debugAdd) cout << "To start: variable " << colno[0] << " - variable " << colno[1] << " = 0.0\n";
		if (debugAdd) cout << "Then:\n";
		map<int, ActionEffectUponVariable> & currMap = preprocessedData[i];
		
		map<int, ActData>::iterator actItr = actionVars.begin();
		const map<int, ActData>::iterator actEnd = actionVars.end();
	
		map<int, ActionEffectUponVariable>::iterator mItr = currMap.begin();
		const map<int, ActionEffectUponVariable>::iterator mEnd = currMap.end();


		while (actItr != actEnd && mItr != mEnd) {
			if (actItr->first < mItr->first) {
				++actItr;
			} else if (mItr->first < actItr->first) {
				++mItr;
			} else {
				colno[arrSize] = actItr->second.Avar;
				actWeight[arrSize] = mItr->second.change;

				if (debugAdd) cout << "\t" << actWeight[arrSize] << "*" << colno[arrSize] << " (" << *(RPGBuilder::getInstantiatedOp(mItr->first)) << ") ";
				if (debugAdd) cout << "[" << get_lowbo(lp, colno[arrSize]) << "," << get_upbo(lp, colno[arrSize]) << "]";


				if (mItr->second.isAssignment) {
					assActWeight[assSize] = 1.0;
					assColno[assSize] = colno[arrSize];
					++assSize;
					if (debugAdd) cout << " (assignment)";

				}

				if (debugAdd) cout << "\n";

				++arrSize;
				++actItr;
				++mItr;
			}
		}
//		cout << "Final constraint of size " << arrSize << "\n";
		add_constraintex(lp, arrSize, actWeight, colno, EQ, 0);
		if (assSize) {
			add_constraintex(lp, assSize, assActWeight, assColno, LE, 1);
		}
		
	}
	
};

void MILPRPG::fillMinMaxFluentTable(vector<double> & toFill) {

	cout << "|";
	cout.flush();
//	static char buf[256];
	static REAL maximise[1];
	maximise[0] = 1.0;
	static int optVar[1];
//	map<double, vector<VarData>, EpsilonComp>::iterator fItr = minMaxVars.find(ts);
//	assert(fItr != minMaxVars.end());

	// bear in mind caching results to maximise/minimise each var, and use those to seed past layers

	vector<VarData> & fVars = minMaxVars.rbegin()->second;

	for (int i = 0; i < varCount; ++i) {
		
//		cout << "Maximising " << *(RPGBuilder::getPNE(i)) << "\n";
		
		optVar[0] = fVars[i].Vvar;
		
//		cout << "Objective function: maximise " << maximise[0] << " * var " << optVar[0] << "\n";
		set_maxim(lp);
//		maximise[0] = -1.0;
		set_obj_fnex(lp, 1, maximise, optVar);
		solve(lp);
	 	const double mv = get_objective(lp);
		toFill[i] = mv;
		set_upbo(lp, optVar[0], mv);
//		cout << "Result = " << toFill[i] << "\n";
		
//		cout << "Minimising " << *(RPGBuilder::getPNE(i)) << "\n";

		set_minim(lp);
//		maximise[0] = 1.0;
		set_obj_fnex(lp, 1, maximise, optVar);
		solve(lp);
		const double mvTwo = get_objective(lp);
		toFill[i + varCount] = -mvTwo;
		set_lowbo(lp, optVar[0], mvTwo);
//		cout << "Result = " << -(toFill[i + varCount]) << "\n";
	}

}

};
