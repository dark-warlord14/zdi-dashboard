# ZDI-23-1532: Ivanti Endpoint Manager ProcessEPMAuthToken Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1532
- **ZDI-CAN:** ZDI-CAN-21852
- **Date:** 2023-10-05
- **CVE:** CVE-2023-28323
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1532/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ProcessEPMAuthToken method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/SA-2023-06-20-CVE-2023-28323?language=en_US

## Disclosure Timeline

- 2023-08-09 - Vulnerability reported to vendor
- 2023-10-05 - Coordinated public release of advisory
