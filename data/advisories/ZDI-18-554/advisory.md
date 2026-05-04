# ZDI-18-554: GE MDS PulseNET IntegrationXMLProcessorServlet UpdateProblemTickets XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-554
- **ZDI-CAN:** ZDI-CAN-5540
- **Date:** 2018-06-07
- **CVE:** CVE-2018-10613
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** GE
- **Affected Products:** MDS PulseNET
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-554/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of GE MDS PulseNET. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the UpdateProblemTickets method of the IntegrationXMLProcessorServlet servlet. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information under the context of the service.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-151-02

## Disclosure Timeline

- 2018-01-05 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
