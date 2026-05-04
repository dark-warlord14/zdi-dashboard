# ZDI-21-067: SolarWinds Orion Platform NCM VulnerabilitySettings Directory Traversal Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-067
- **ZDI-CAN:** ZDI-CAN-11902
- **Date:** 2021-09-20
- **CVE:** CVE-2020-27871
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-067/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of SolarWinds Orion Platform. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within VulnerabilitySettings.aspx. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in Orion Platform 2020.2.1 Hot Fix 2 - released on 12/15/2020

## Disclosure Timeline

- 2020-10-14 - Vulnerability reported to vendor
- 2021-09-20 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
