# ZDI-22-785: Ivanti Avalanche EnterpriseServer Service Race Condition Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-785
- **ZDI-CAN:** ZDI-CAN-15528
- **Date:** 2022-05-26
- **CVE:** CVE-2022-36980
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-785/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Ivanti Avalanche. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the EnterpriseServer service. The issue results from the lack of proper locking when performing operations during authentication. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://download.wavelink.com/Files/avalanche_v6.3.4_release_notes.txt

## Disclosure Timeline

- 2021-11-10 - Vulnerability reported to vendor
- 2022-05-26 - Coordinated public release of advisory
- 2022-07-27 - Advisory Updated
