# ZDI-25-916: Linux Kernel ksmbd smb2_sess_setup Preauth_HashValue Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-916
- **ZDI-CAN:** ZDI-CAN-27661
- **Date:** 2025-09-24
- **CVE:** CVE-2025-38561
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-916/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the Preauth_HashValue field. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=44a3059c4c8cc635a1fb2afd692d0730ca1ba4b6

## Disclosure Timeline

- 2025-07-22 - Vulnerability reported to vendor
- 2025-09-24 - Coordinated public release of advisory
- 2025-09-24 - Advisory Updated
