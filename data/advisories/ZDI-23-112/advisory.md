# ZDI-23-112: (Pwn2Own) Western Digital MyCloud PR4100 FTP Server Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-112
- **ZDI-CAN:** ZDI-CAN-19736
- **Date:** 2023-02-09
- **CVE:** CVE-2022-29844
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Luca MORO (@johncool__)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-112/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Western Digital MyCloud PR4100 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FTP server. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-23002-my-cloud-firmware-version-5-26-119

## Disclosure Timeline

- 2022-12-29 - Vulnerability reported to vendor
- 2023-02-09 - Coordinated public release of advisory
