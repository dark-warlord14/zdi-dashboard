# ZDI-16-616: Hewlett Packard Enterprise Network Automation RPCServlet Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-616
- **ZDI-CAN:** ZDI-CAN-3729
- **Date:** 2016-11-30
- **CVE:** CVE-2016-8511
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Network Automation
- **Credit:** Jacob Baines Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-616/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Network Automation. Authentication is not required to exploit this vulnerability. The specific flaw exists within the exposed RPCServlet. By sending a crafted request, the application can be made to deserialize untrusted data. An attacker can leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-c05344849

## Disclosure Timeline

- 2016-07-18 - Vulnerability reported to vendor
- 2016-11-30 - Coordinated public release of advisory
