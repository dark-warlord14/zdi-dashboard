# ZDI-23-082: Delta Electronics InfraSuite Device Master CtrlLayerNWCmd_FileOperation Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-082
- **ZDI-CAN:** ZDI-CAN-19414
- **Date:** 2023-01-18
- **CVE:** CVE-2022-41657
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-082/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Delta Electronics InfraSuite Device Master. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the CtrlLayerNWCmd_FileOperation function. When parsing the fileName element, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-298-07

## Disclosure Timeline

- 2022-11-10 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
