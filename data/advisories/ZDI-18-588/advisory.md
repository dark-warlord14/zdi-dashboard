# ZDI-18-588: Delta Industrial Automation COMMGR AHSIM_5x0 Simulator Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-588
- **ZDI-CAN:** ZDI-CAN-5667
- **Date:** 2018-06-26
- **CVE:** CVE-2018-10594
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** COMMGR
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-588/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation COMMGR. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of TCP packets sent to the AHSIM 5x0 Simulator. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the COMMGR process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-172-01

## Disclosure Timeline

- 2018-02-23 - Vulnerability reported to vendor
- 2018-06-26 - Coordinated public release of advisory
- 2018-06-26 - Advisory Updated
