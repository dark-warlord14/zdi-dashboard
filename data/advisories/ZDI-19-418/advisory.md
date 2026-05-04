# ZDI-19-418: Delta Industrial Automation CNCSoft ScreenEditor DPB File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-418
- **ZDI-CAN:** ZDI-CAN-8059
- **Date:** 2019-04-17
- **CVE:** CVE-2019-10949
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** CNCSoft
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-418/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Delta Industrial Automation CNCSoft ScreenEditor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPB files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the Administrator.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-106-01

## Disclosure Timeline

- 2019-02-07 - Vulnerability reported to vendor
- 2019-04-17 - Coordinated public release of advisory
