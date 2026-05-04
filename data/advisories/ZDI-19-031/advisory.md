# ZDI-19-031: Schneider Electric IIoT Monitor Hard-coded Cryptographic Key Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-031
- **ZDI-CAN:** ZDI-CAN-7119
- **Date:** 2019-01-16
- **CVE:** CVE-2018-7839
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IIot Monitor
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-031/
## Vulnerability Details

This vulnerability allows the decryption of the administrator password on vulnerable installations of Schneider Electric IIoT Monitor. Authentication is not required to exploit this vulnerability. The specific flaw exists within encryption of the administrator password in the AESEncryption class. A hard-coded cryptographic key is used which can allow the reversal of the encryption process. An attacker can leverage this vulnerability in conjunction with other vulnerabilities to bypass authentication on the system.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-008-02

## Disclosure Timeline

- 2018-08-14 - Vulnerability reported to vendor
- 2019-01-16 - Coordinated public release of advisory
