# ZDI-20-1453: Qognify Ocularis EventCoordinator ConnectedChannel_GotMessage Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1453
- **ZDI-CAN:** ZDI-CAN-11257
- **Date:** 2020-12-29
- **CVE:** CVE-2020-27868
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Qognify
- **Affected Products:** Ocularis
- **Credit:** Joachim Kerschbaumer (@joachimk)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1453/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Qognify Ocularis. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of serialized objects provided to the EventCoordinator endpoint. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Qognify has issued an update to correct this vulnerability. More details can be found at: https://www.qognify.com/support-training/software-downloads/

## Disclosure Timeline

- 2020-07-14 - Vulnerability reported to vendor
- 2020-12-29 - Coordinated public release of advisory
- 2021-03-04 - Advisory Updated
