# ZDI-18-549: GE MDS PulseNET ToolingService Deserialization Of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-549
- **ZDI-CAN:** ZDI-CAN-5537
- **Date:** 2018-06-06
- **CVE:** CVE-2018-10611
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** GE
- **Affected Products:** MDS PulseNET
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-549/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of GE MDS PulseNET. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the ToolingService web service. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code under the context of the current web service.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-151-02

## Disclosure Timeline

- 2018-01-10 - Vulnerability reported to vendor
- 2018-06-06 - Coordinated public release of advisory
- 2018-06-06 - Advisory Updated
