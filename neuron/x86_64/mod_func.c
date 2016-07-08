#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _kdrca1_reg(void);
extern void _na3_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," kdrca1.mod");
    fprintf(stderr," na3.mod");
    fprintf(stderr, "\n");
  }
  _kdrca1_reg();
  _na3_reg();
}
