# ZDI-24-844: (Pwn2Own) Alpine Halo9 prh_l2_sar_data_ind Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-844
- **ZDI-CAN:** ZDI-CAN-22945
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23923
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Alpine
- **Affected Products:** Halo9
- **Credit:** PCAutomotive
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-844/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Alpine Halo9 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the prh_l2_sar_data_ind function. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Alpine conducted a Threat Assessment and Remediation Analysis (TARA) in accordance with ISO21434, and concluded that the vulnerability is classified as "Sharing the Risk". Alpine states that they will continue to use the current software without a releasing patch.

## Disclosure Timeline

- 2024-02-01 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
