# ZDI-17-199: Trend Micro InterScan Web Security Virtual Appliance LogDelete processRequest method Directory Traversal Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-199
- **ZDI-CAN:** ZDI-CAN-4311
- **Date:** 2017-03-29
- **CVE:** N/A
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:N/I:N/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-199/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is required to exploit this vulnerability. The specific flaw exists within the LogDelete processRequest method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to deny service to users of the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116960

## Disclosure Timeline

- 2016-12-20 - Vulnerability reported to vendor
- 2017-03-29 - Coordinated public release of advisory
