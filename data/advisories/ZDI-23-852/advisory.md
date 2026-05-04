# ZDI-23-852: (Pwn2Own) Western Digital MyCloud PR4100 account_mgr Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-852
- **ZDI-CAN:** ZDI-CAN-20003
- **Date:** 2023-06-08
- **CVE:** CVE-2022-29842
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Sam Thomas (@_s_n_t) of Pentest Ltd (@pentestltd)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-852/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Western Digital MyCloud PR4100 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the account_mgr cgi script. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-23002-my-cloud-firmware-version-5-26-119

## Disclosure Timeline

- 2022-12-29 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
