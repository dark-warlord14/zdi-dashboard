# ZDI-22-776: Ivanti Avalanche JwtTokenUtility Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-776
- **ZDI-CAN:** ZDI-CAN-15301
- **Date:** 2022-05-26
- **CVE:** CVE-2022-36971
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-776/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Avalanche. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the JwtTokenUtility class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://download.wavelink.com/Files/avalanche_v6.3.4_release_notes.txt

## Disclosure Timeline

- 2021-10-22 - Vulnerability reported to vendor
- 2022-05-26 - Coordinated public release of advisory
- 2022-07-27 - Advisory Updated
