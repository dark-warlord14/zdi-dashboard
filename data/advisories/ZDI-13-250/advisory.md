# ZDI-13-250: PANDA Security Communications Agent Service Pagent.exe 'MESSAGE_FROM_REMOTE' Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-250
- **ZDI-CAN:** ZDI-CAN-1762
- **Date:** 2013-10-16
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Panda Software
- **Affected Products:** Security for Business Communications
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-250/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of PANDA Security for Business Communications. Authentication is not required to exploit this vulnerability. The specific flaw exists within the 'Panda AdminSecure Communications Agent' (Pagent.exe) which listens on tcp port 19226. The service contains a directory traversal flaw which allows for the ability to create / overwrite / delete an arbitrary file. A remote attacker can abuse this to execute remote code under the context of the SYSTEM user.

## Additional Details

Panda Software has issued an update to correct this vulnerability. More details can be found at: http://www.pandasecurity.com/enterprise/support/card?id=40081

## Disclosure Timeline

- 2013-07-05 - Vulnerability reported to vendor
- 2013-10-16 - Coordinated public release of advisory
