# ZDI-26-193: (Pwn2Own) Linux Kernel nf_tables_newset Out-Of-Bounds Write Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-193
- **ZDI-CAN:** ZDI-CAN-17464
- **Date:** 2026-03-16
- **CVE:** CVE-2022-1972
- **CVSS:** 3.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Team Orca of Sea Security (@seasecresponse), security.sea.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-193/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of nft_objects. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilties to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://ubuntu.com/security/CVE-2022-2078#notes

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
