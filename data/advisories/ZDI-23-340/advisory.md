# ZDI-23-340: Schneider Electric IGSSdataServer Exposed Dangerous Function Data Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-340
- **ZDI-CAN:** ZDI-CAN-19531
- **Date:** 2023-03-16
- **CVE:** CVE-2023-27983
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-340/
## Vulnerability Details

This vulnerability allows remote attackers to delete application-level data on affected installations of Schneider Electric IGSS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IGSSdataServer process, which listens on TCP port 12401 by default. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to delete application-specific data.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2023-073-04&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2023-073-04.pdf

## Disclosure Timeline

- 2023-01-07 - Vulnerability reported to vendor
- 2023-03-16 - Coordinated public release of advisory
