# ZDI-18-228: Delta Industrial Automation DOPSoft DPA File ButtonOnMacro Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-228
- **ZDI-CAN:** ZDI-CAN-5274
- **Date:** 2018-03-02
- **CVE:** CVE-2018-5476
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DOPSoft
- **Credit:** Ghirmay Desta
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-228/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation DOPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the ButtonOnMacro structure in a DPA file. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-060-03

## Disclosure Timeline

- 2017-10-12 - Vulnerability reported to vendor
- 2018-03-02 - Coordinated public release of advisory
- 2018-03-02 - Advisory Updated
