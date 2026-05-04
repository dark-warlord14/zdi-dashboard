# ZDI-08-052: OpenLDAP BER Decoding Remote DoS Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-052
- **ZDI-CAN:** ZDI-CAN-347
- **Date:** 2008-08-14
- **CVE:** CVE-2008-2952
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** OpenLDAP Foundation
- **Affected Products:** OpenLDAP
- **Credit:** Oscar Mira-Sanchez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-052/
## Vulnerability Details

This vulnerability allows remote attackers to deny services on vulnerable installations of OpenLDAP. Authentication is not required to exploit this vulnerability. The specific flaw exists in the decoding of ASN.1 BER network datagrams. When the size of a BerElement is specified incorrectly, the application will trigger an assert(), leading to abnormal program termination.

## Additional Details

OpenLDAP Foundation has issued an update to correct this vulnerability. More details can be found at: http://www.openldap.org/software/release/changes.html

## Disclosure Timeline

- 2008-06-26 - Vulnerability reported to vendor
- 2008-08-14 - Coordinated public release of advisory
