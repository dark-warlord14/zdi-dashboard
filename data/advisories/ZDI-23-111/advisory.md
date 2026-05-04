# ZDI-23-111: (Pwn2Own) Western Digital MyCloud PR4100 DDNS Response Processing Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-111
- **ZDI-CAN:** ZDI-CAN-19694
- **Date:** 2023-02-09
- **CVE:** CVE-2022-29843
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** rskvp93 and biennd4 (from VcsLab of Viettel Cyber Security)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-111/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Western Digital MyCloud PR4100. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of DDNS responses. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-23002-my-cloud-firmware-version-5-26-119

## Disclosure Timeline

- 2023-01-21 - Vulnerability reported to vendor
- 2023-02-09 - Coordinated public release of advisory
