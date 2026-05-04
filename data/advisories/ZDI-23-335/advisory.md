# ZDI-23-335: Schneider Electric IGSS IGSSdataServer Exposed Dangerous Function Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-335
- **ZDI-CAN:** ZDI-CAN-19654
- **Date:** 2023-03-16
- **CVE:** CVE-2023-27977
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:L
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-335/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Schneider Electric IGSS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IGSSdataServer process, which listens on TCP port 12401 by default. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2023-073-04&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2023-073-04.pdf

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-03-16 - Coordinated public release of advisory
