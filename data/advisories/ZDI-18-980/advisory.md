# ZDI-18-980: Delta Industrial Automation CNCSoft ScreenEditor DPB File TextBank wText Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-980
- **ZDI-CAN:** ZDI-CAN-6269
- **Date:** 2018-09-05
- **CVE:** CVE-2018-10636
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** CNCSoft
- **Credit:** Natnael Samson(Natti)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-980/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation CNCSoft ScreenEditor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DPB files. When parsing the TextBank wText attribute, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of Administrator.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-219-01

## Disclosure Timeline

- 2018-05-29 - Vulnerability reported to vendor
- 2018-09-05 - Coordinated public release of advisory
- 2018-09-05 - Advisory Updated
