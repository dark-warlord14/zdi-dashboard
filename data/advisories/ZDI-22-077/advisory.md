# ZDI-22-077: (Pwn2Own) Western Digital MyCloud PR4100 ConnectivityService Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-077
- **ZDI-CAN:** ZDI-CAN-15856
- **Date:** 2022-01-17
- **CVE:** CVE-2022-22991
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Martin Rakhmanov (@mrakhmanov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-077/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Western Digital MyCloud PR4100. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ConnectivityService service. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-22002-my-cloud-os5-firmware-5-19-117

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-01-17 - Coordinated public release of advisory
- 2022-01-18 - Advisory Updated
