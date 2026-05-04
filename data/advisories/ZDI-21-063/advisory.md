# ZDI-21-063: SolarWinds Network Performance Monitor ExecuteExternalProgram Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-063
- **ZDI-CAN:** ZDI-CAN-11858
- **Date:** 2021-09-20
- **CVE:** CVE-2020-14005
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Performance Monitor
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-063/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Network Performance Monitor. Authentication is required to exploit this vulnerability. The specific flaw exists within the ExecuteExternalProgram method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of system.

## Additional Details

Fixed in Orion Platform 2020.2.1 Hot Fix 2 - released on 12/15/2020

## Disclosure Timeline

- 2020-09-30 - Vulnerability reported to vendor
- 2021-09-20 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
