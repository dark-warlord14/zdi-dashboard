# ZDI-19-305: Jaspersoft JasperReports Server DiagnosticDataCipherer Hard-coded Cryptographic Key Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-305
- **ZDI-CAN:** ZDI-CAN-7654
- **Date:** 2019-04-02
- **CVE:** CVE-2018-18815
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Jaspersoft
- **Affected Products:** Jasper Reports
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-305/
## Vulnerability Details

This vulnerability allows the decryption of the passwords on vulnerable installations of Jaspersoft JasperReports Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within encryption of user passwords in the DiagnosticDataCipherer class. A hard-coded cryptographic key is used which can allow the reversal of the encryption process. An attacker can leverage this vulnerability in conjunction with other vulnerabilities to bypass authentication on the system.

## Additional Details

Jaspersoft has issued an update to correct this vulnerability. More details can be found at: https://www.tibco.com/support/advisories/2019/03/tibco-security-advisory-march-6-2019-tibco-jasperreports-server-2018-18815

## Disclosure Timeline

- 2018-12-10 - Vulnerability reported to vendor
- 2019-04-02 - Coordinated public release of advisory
