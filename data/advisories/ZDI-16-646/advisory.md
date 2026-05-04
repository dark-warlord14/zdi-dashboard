# ZDI-16-646: Delta Industrial Automation WPLSoft Heap Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-646
- **ZDI-CAN:** ZDI-CAN-3587
- **Date:** 2016-12-15
- **CVE:** CVE-2016-5802
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** WPLSoft
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-646/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation WPLSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing of a dvp file. A malformed dvp file can cause heap corruption and the BorrlndmmSysGetMem function will write to an arbitrary memory location in the user process. A remote attacker could leverage this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-348-03

## Disclosure Timeline

- 2016-09-19 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
