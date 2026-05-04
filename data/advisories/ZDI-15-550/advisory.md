# ZDI-15-550: Oracle Beehive prepareAudioToPlay Arbitrary File Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-550
- **ZDI-CAN:** ZDI-CAN-3004
- **Date:** 2015-11-10
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Beehive
- **Credit:** Steven Seeley of Source Incite & sinn3r of Rapid7
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-550/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Beehive. Authentication is not required to exploit this vulnerability. The specific flaw exists within the voice-servlet's playAudioFile.jsp. The method prepareAudioToPlay contains vulnerable parameters allowing for an attacker to write arbitrary content to the web application. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuoct2015-2367953.html

## Disclosure Timeline

- 2015-06-30 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
