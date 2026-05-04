# ZDI-12-094: RealNetworks Helix Server rn5auth Credential Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-094
- **ZDI-CAN:** ZDI-CAN-1428
- **Date:** 2012-06-21
- **CVE:** CVE-2012-0942
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** Helix Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-094/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Real Helix Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within rn4auth.dll, which is responsible for parsing authentication credentials. When the GetNameValuePair() function calls strcpy, there is an unbounded copy into a stack buffer, which can lead to stack memory corruption. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://helixproducts.real.com/docs/security/SecurityUpdate04022012HS.pdf

## Disclosure Timeline

- 2011-11-04 - Vulnerability reported to vendor
- 2012-06-21 - Coordinated public release of advisory
