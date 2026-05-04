# ZDI-22-1691: Linux Kernel ksmbd Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1691
- **ZDI-CAN:** ZDI-CAN-17817
- **Date:** 2023-01-23
- **CVE:** CVE-2022-47943
- **CVSS:** 9.6
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Arnaud Gatignol, Quentin Minster, Florent Saudel, Guillaume Teissier (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1691/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of SMB2_WRITE commands. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=ac60778b87e45576d7bfdbd6f53df902654e6f09

## Disclosure Timeline

- 2022-07-26 - Vulnerability reported to vendor
- 2023-01-23 - Coordinated public release of advisory
- 2023-03-21 - Advisory Updated
