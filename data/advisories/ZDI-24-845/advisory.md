# ZDI-24-845: (Pwn2Own) Alpine Halo9 Improper Verification of Cryptographic Signature Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-845
- **ZDI-CAN:** ZDI-CAN-23102
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23960
- **CVSS:** 4.6
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Alpine
- **Affected Products:** Halo9
- **Credit:** NCC Group EDG (@nccgroupinfosec @_mccaulay @alexjplaskett)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-845/
## Vulnerability Details

This vulnerability allows physically present attackers to bypass signature validation mechanism on affected installations of Alpine Halo9 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the firmware metadata signature validation mechanism. The issue results from the lack of proper verification of a cryptographic signature. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Alpine conducted a Threat Assessment and Remediation Analysis (TARA) in accordance with ISO21434, and concluded that the vulnerability is classified as "Sharing the Risk". Alpine states that they will continue to use the current software without a releasing patch.

## Disclosure Timeline

- 2024-02-01 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
