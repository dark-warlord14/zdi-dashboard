# ZDI-18-964: Trend Micro OfficeScan Named Pipe Request Processing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-964
- **ZDI-CAN:** ZDI-CAN-6104
- **Date:** 2018-08-30
- **CVE:** CVE-2018-15364
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:N/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** OfficeScan
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-964/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Trend Micro OfficeScan. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of data from a named pipe in Ntrtscan.exe. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges to SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1120678

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-08-30 - Coordinated public release of advisory
- 2018-08-30 - Advisory Updated
