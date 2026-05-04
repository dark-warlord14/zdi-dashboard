# ZDI-22-244: Samba AppleDouble Entry Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-244
- **ZDI-CAN:** ZDI-CAN-16156
- **Date:** 2022-02-01
- **CVE:** CVE-2021-44142
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samba
- **Affected Products:** Samba
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-244/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samba. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of AppleDouble entries. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Samba has issued an update to correct this vulnerability. More details can be found at: https://www.samba.org/samba/security/CVE-2021-44142.html

## Disclosure Timeline

- 2021-12-15 - Vulnerability reported to vendor
- 2022-02-01 - Coordinated public release of advisory
