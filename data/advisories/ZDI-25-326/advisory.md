# ZDI-25-326: (0Day) (Pwn2Own) WOLFBOX Level 2 EV Charger MCU Command Parsing Misinterpretation of Input Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-326
- **ZDI-CAN:** ZDI-CAN-26501
- **Date:** 2025-06-06
- **CVE:** CVE-2025-5747
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** WOLFBOX
- **Affected Products:** Level 2 EV Charger
- **Credit:** PHP Hooligans
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-326/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installatons of WOLFBOX Level 2 EV Charger devices. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of command frames received by the MCU. When parsing frames, the process does not properly detect the start of a frame, which can lead to misinterpretation of input. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the device.

## Additional Details

ZDI made several attempts to contact the vendor using the contact information on their website, as well as trying to reach them on various social platforms which yielded no response. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-05-15 - Vulnerability reported to vendor
- 2025-06-06 - Coordinated public release of advisory
- 2025-06-06 - Advisory Updated
