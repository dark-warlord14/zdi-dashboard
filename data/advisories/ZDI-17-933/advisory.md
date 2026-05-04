# ZDI-17-933: Cisco WebEx Network Recording Player Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-933
- **ZDI-CAN:** ZDI-CAN-5041
- **Date:** 2017-12-06
- **CVE:** CVE-2017-12372
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-933/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Network Recording Player. Authentication is not required to exploit this vulnerability. The specific flaw exists within the wbx URI handler. When parsing the register parameter, the process does not properly validate a user-supplied string before using it to execute a system command. An attacker can leverage this vulnerability to execute commands under the context of the current user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20171129-webex-players

## Disclosure Timeline

- 2017-08-10 - Vulnerability reported to vendor
- 2017-12-06 - Coordinated public release of advisory
