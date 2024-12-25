#include "C_Code.h" // headers 

void UnitExpGainTosC(u8 pid) {
	int exp;
	exp = PidStatsGetExpGain(pid);
	SetEventSlotC(exp);
}