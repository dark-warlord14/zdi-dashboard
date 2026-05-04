# ZDI-15-033: Motorola Scanner SDK OPOSSCANNER.ocx Open Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-033
- **ZDI-CAN:** ZDI-CAN-2489
- **Date:** 2015-02-10
- **CVE:** CVE-2015-1495
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Motorola
- **Affected Products:** Scanner SDK
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-033/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Motorola Scanner SDK. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the IOPOSScanner Open method which performs an unbounded string copy operation into a fixed-length stack buffer using attacker-supplied input. A remote attacker can leverage this to execute arbitrary code under the context of the browser process.

## Additional Details

Motorola has issued an update to correct this vulnerability. More details can be found at: https://portal.motorolasolutions.com/Support/US-EN/Resolution?solutionId=87666&redirectForm=search&searchQuery=%3FsearchType%3Dsimple%26searchTerm%3Dscanner%20sdk

## Disclosure Timeline

- 2014-10-10 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
