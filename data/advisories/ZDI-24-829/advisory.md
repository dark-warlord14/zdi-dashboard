# ZDI-24-829: (Pwn2Own) Samsung Galaxy S23 McsWebViewActivity Permissive List of Allowed Inputs Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-829
- **ZDI-CAN:** ZDI-CAN-22409
- **Date:** 2024-06-21
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S23
- **Credit:** Nguyen Tien Giang & Nguyen Hoang Thach of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-829/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung Galaxy S23 smartphones. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the McsWebViewActivity class. The issue results from a permissive list of allowed inputs. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Server Side Fix in SVE-2023-1953.

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
