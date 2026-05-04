# ZDI-24-849: (Pwn2Own) Alpine Halo9 UPDM_wemCmdUpdFSpeDecomp Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-849
- **ZDI-CAN:** ZDI-CAN-23306
- **Date:** 2024-06-21
- **CVE:** CVE-2024-23961
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Alpine
- **Affected Products:** Halo9
- **Credit:** NCC Group EDG (@nccgroupinfosec @_mccaulay @alexjplaskett)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-849/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Alpine Halo9 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UPDM_wemCmdUpdFSpeDecomp function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Alpine conducted a Threat Assessment and Remediation Analysis (TARA) in accordance with ISO21434, and concluded that the vulnerability is classified as "Sharing the Risk". Alpine states that they will continue to use the current software without a releasing patch.

## Disclosure Timeline

- 2024-02-01 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
