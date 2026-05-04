# ZDI-21-153: Micro Focus Operations Bridge Reporter userName Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-153
- **ZDI-CAN:** ZDI-CAN-11074
- **Date:** 2021-02-09
- **CVE:** CVE-2021-22502
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Micro Focus
- **Affected Products:** Operations Bridge Reporter
- **Credit:** Pedro Ribeiro (pedrib@gmail.com|@pedrib1337) from Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-153/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Micro Focus Operations Bridge Reporter. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the userName parameter provided to the LogonResource endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Micro Focus has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.softwaregrp.com/doc/KM03775947

## Disclosure Timeline

- 2020-09-30 - Vulnerability reported to vendor
- 2021-02-09 - Coordinated public release of advisory
