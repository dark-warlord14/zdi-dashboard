# ZDI-11-085: Oracle Java XGetSamplePtrFromSnd Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-085
- **ZDI-CAN:** ZDI-CAN-945
- **Date:** 2011-02-15
- **CVE:** CVE-2010-4462
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-085/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within jsound!XGetSamplePtrFromSnd. When extracting a sample from a soundbank stream user supplied data is used to calculate the bounds of a call to PV_Swap16BitSamples. By supplying a specially crafted sound file, a remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2011-304611.html

## Disclosure Timeline

- 2010-09-23 - Vulnerability reported to vendor
- 2011-02-15 - Coordinated public release of advisory
