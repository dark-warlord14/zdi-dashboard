# ZDI-22-076: (Pwn2Own) Western Digital MyCloud PR4100 cloudAccess Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-076
- **ZDI-CAN:** ZDI-CAN-15872
- **Date:** 2022-01-17
- **CVE:** CVE-2022-22992
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Sam Thomas (@_s_n_t) of Pentest Ltd (@pentestltd)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-076/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Western Digital MyCloud PR4100. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the cloudAccess endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-22002-my-cloud-os5-firmware-5-19-117

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-01-17 - Coordinated public release of advisory
- 2022-02-10 - Advisory Updated
