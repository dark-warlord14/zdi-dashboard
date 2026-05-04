# ZDI-23-843: (Pwn2Own) Samsung Galaxy S22 McsWebViewActivity Permissive List of Allowed Inputs Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-843
- **ZDI-CAN:** ZDI-CAN-19699
- **Date:** 2023-06-08
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S22
- **Credit:** Nguyen Tien Giang (@testanull), Nguyen Hoang Thach (@hi_im_d4rkn3ss) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-843/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung Galaxy S22 smartphones. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the McsWebViewActivity class. The issue results from a permissive list of allowed inputs. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Patched in the December 2022 Galaxy Store server-side update.

## Disclosure Timeline

- 2023-01-24 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
