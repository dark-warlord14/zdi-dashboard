# ZDI-10-175: Hewlett-Packard Data Protector Express PrvRecvRqu Remote Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-175
- **ZDI-CAN:** ZDI-CAN-582
- **Date:** 2010-09-13
- **CVE:** CVE-2010-3008
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Data Protector
- **Credit:** AbdulAziz Hariri of Insight Technologies
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-175/
## Vulnerability Details

This vulnerability allows remote attackers to trigger a denial of service condition on vulnerable installations of Hewlett-Packard Data Protector. Authentication is not required to exploit this vulnerability. The specific flaw exists within the function PrvRecvRqu() defined in the module dpwinsup. While handling requests sent to TCP port 3817 the process can be forced to dereference a NULL pointer resulting in an unhandled exception that crashes the service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02067559

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-09-13 - Coordinated public release of advisory
