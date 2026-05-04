# ZDI-21-277: Western Digital MyCloud PR4100 Link Resolution Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-277
- **ZDI-CAN:** ZDI-CAN-12455
- **Date:** 2021-03-11
- **CVE:** CVE-2021-3310
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Chris Hernandez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-277/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Western Digital MyCloud PR4100. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SMB and AFP services. By creating a symbolic link, an attacker can abuse the service to read arbitrary files. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/productsecurity/wdc-21002-my-cloud-firmware-version-5-10-122

## Disclosure Timeline

- 2021-01-05 - Vulnerability reported to vendor
- 2021-03-11 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
