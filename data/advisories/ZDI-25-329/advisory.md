# ZDI-25-329: (0Day) (Pwn2Own) WOLFBOX Level 2 EV Charger tuya_svc_devos_activate_result_parse Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-329
- **ZDI-CAN:** ZDI-CAN-26294
- **Date:** 2025-06-06
- **CVE:** CVE-2025-5750
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** WOLFBOX
- **Affected Products:** Level 2 EV Charger
- **Credit:** Rafal Goryl of PixiePoint Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-329/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of WOLFBOX Level 2 EV Charger. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the secKey, localKey, stdTimeZone and devId parameters. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

ZDI made several attempts to contact the vendor using the contact information on their website, as well as trying to reach them on various social platforms which yielded no response. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-03-10 - Vulnerability reported to vendor
- 2025-06-06 - Coordinated public release of advisory
- 2025-06-06 - Advisory Updated
