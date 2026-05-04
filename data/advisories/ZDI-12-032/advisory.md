# ZDI-12-032: Oracle Java Runtime Environment readMabCurveData Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-032
- **ZDI-CAN:** ZDI-CAN-1353
- **Date:** 2012-02-22
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Alin Rad Pop (binaryproof)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-032/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle's Java Runtime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses structures for a specific tag descriptor with a specific ICC color profile. When handling a field from this structure, the application will incorrectly check for signedness and then perform an operation on it. This will then get passed to an allocation. Immediately following this, the application will use a different size to initialize the allocation. This can lead to a controllable memory corruption which can be leveraged to achieve code execution under the context of the applicaiton.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2012-366318.html

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-02-22 - Coordinated public release of advisory
