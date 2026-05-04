# ZDI-20-1080: Senstar Symphony SSOAuth Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1080
- **ZDI-CAN:** ZDI-CAN-10980
- **Date:** 2020-08-26
- **CVE:** CVE-2020-17405
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Senstar
- **Affected Products:** Symphony
- **Credit:** Joachim Kerschbaumer (@joachimk)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1080/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Senstar Symphony. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SSOAuth process. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Fixed in version 7.4.1

## Disclosure Timeline

- 2020-05-27 - Vulnerability reported to vendor
- 2020-08-26 - Coordinated public release of advisory
