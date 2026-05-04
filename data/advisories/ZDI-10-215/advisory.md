# ZDI-10-215: IBM Informix Dynamic Server librpc.dll Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-215
- **ZDI-CAN:** ZDI-CAN-200
- **Date:** 2010-10-18
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Informix
- **Credit:** Sebastian Apelt (sebastian.apelt@siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-215/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of IBM Informix Dynamic Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RPC protocol parsing library, librpc.dll, utilized by the ISM Portmapper service (portmap.exe) bound by default to TCP port 36890. A lack of sanity checking on supplied parameter sizes can result in an integer overflow and subsequent heap buffer under allocation which can finally lead to an exploitable memory corruption.

## Additional Details

this issue was fixed in ISM 2.20.TC1.117 Integrated into the following versions by defect# idsdb00146931 - 7.31.xD11 idsdb00146930 - 9.40.xC10 idsdb00146929 - 10.00.xC8 idsdb00138308 - 11.10.xC2 This was fixed before 11.50 went GA; the fix is also in 11.50.

## Disclosure Timeline

- 2007-05-22 - Vulnerability reported to vendor
- 2010-10-18 - Coordinated public release of advisory
