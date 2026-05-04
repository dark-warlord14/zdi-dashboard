# ZDI-23-848: (Pwn2Own) Western Digital MyCloud PR4100 restsdk Directory Traversal Arbitrary File Read and Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-848
- **ZDI-CAN:** ZDI-CAN-19862
- **Date:** 2023-06-08
- **CVE:** CVE-2022-36328
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-848/
## Vulnerability Details

This vulnerability allows remote attackers to create and read arbitrary files on affected installations of Western Digital MyCloud PR4100 NAS devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the restsdk binary. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-23006-my-cloud-firmware-version-5-26-202

## Disclosure Timeline

- 2023-01-25 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
